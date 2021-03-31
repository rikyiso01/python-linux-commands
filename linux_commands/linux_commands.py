from subprocess import run,PIPE
from typing import Iterable,Any,Union,TypeVar,Sequence,List,Tuple
from os import kill,getpid,environ
from sys import stderr

RESULT_TYPE=Union[int,str]

def convert_key(result:List[str],key:str,value:Any):
    argument=f'-{key}' if len(key)==1 else f'--{key}'
    if isinstance(value,bool):
        if value:
            result.append(argument)
    else:
        result.append(argument)
        result.append(value)

def convert_value(value:str)->RESULT_TYPE:
    if value.lstrip('-').isnumeric():
        return int(value)
    else:
        return value


T=TypeVar('T')
def convert_list(value:Sequence[T])->Union[T,Tuple[T,...],None]:
    if len(value)==0:
        return None
    elif len(value)==1:
        return value[0]
    else:
        return tuple(value)

def get_error(code:int,error:str)->Exception:
    if code==2:
        return SyntaxError(error)
    elif code==126:
        return PermissionError(error)
    elif code==127:
        return AttributeError(error)
    elif code==128:
        return TypeError(error)
    elif 129<=code<=165:
        kill(getpid(),code-128)
    elif code==255:
        return TypeError(error)
    else:
        return OSError(error)

class Command:
    def __init__(self,commands:Iterable[str]):
        self.__commands:Tuple[str]=tuple(commands)

    def __call__(self, *args:Any, stdin:str='',env=environ,**kwargs:Any)->Union[RESULT_TYPE,Tuple[RESULT_TYPE],
                                                                                Tuple[Tuple[RESULT_TYPE]],None]:
        command=list(self.__commands)
        for key in kwargs.keys():
            convert_key(command,key,kwargs[key])
        command.extend(str(arg) for arg in args)
        process=run(command,input=stdin,env=env,text=True,stdout=PIPE,stderr=PIPE)
        code=process.returncode
        if code!=0:
            if process.stdout!='':
                print(process.stdout)
            raise get_error(code,process.stderr)
        if process.stderr!='':
            print(process.stderr,file=stderr)
        result:List[RESULT_TYPE,Tuple[RESULT_TYPE,...]]=[]
        for line in process.stdout.splitlines():
            line_values:List[RESULT_TYPE]=[]
            for value in line.split():
                line_values.append(convert_value(value))
            line_values:Union[RESULT_TYPE,Tuple[RESULT_TYPE,...],None]=convert_list(line_values)
            if line_values is not None:
                result.append(line_values)
        return convert_list(result)

    def __getattr__(self, item:str)->'Command':
        return Command([*self.__commands,item])

def __getattr__(name:str)->Command:
    return Command([name])

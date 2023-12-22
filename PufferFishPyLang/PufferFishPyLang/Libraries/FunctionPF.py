'''
fnc function_name (args,args,args) <return_type> <public> <static> 
{
    pr();
}
Basic Function to Print to Console
'''
class Function:
    def __init__(self,name :str,ret_type :any,args : list,stat_pp :str,stat_cs :str) -> None:
        function_name = name
        return_type = ret_type
        statement_pp = stat_pp
        statement_cs = stat_cs
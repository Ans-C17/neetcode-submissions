class Solution:
    def simplifyPath(self, path: str) -> str:
        path_str = path.split('/')
        print(path_str)
        stack = []

        for st in path_str:
            if st == '..':
                if stack:
                    stack.pop()
            elif st != '.' and st != '':
                stack.append(st)
            print(stack)
        
        return '/' + '/'.join(stack)
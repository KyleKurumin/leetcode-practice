class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        output = ['']

        for i in range(len(path)):
            if path[i] == '' or path[i] == '.':
                continue
            elif path[i] == '..' and len(output) > 1:
                output.pop()
            elif path[i] != '..':
                output.append(path[i])

        return '/'.join(output) if len(output) > 1 else '/'

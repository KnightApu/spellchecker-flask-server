class TrieNode():
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.last = False
        
        

    def add(self, word: str):
    
        node = self
    
        for char in word:
            found_in_child = False
        
            for child in node.children:
                if child.char == char:
                    found_in_child = True
                    node = child
                    break
        
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node=new_node
            
        node.last=True
    

    def search(self, word: str):
        node=self
    
        if not node.children:
            return False
        
        for char in word:
            char_not_found=True
        
            for child in node.children:
                if child.char == char:
                    char_not_found=False
                    node=child
                    break
            
            if char_not_found:
                return False
            
    
        return True

    def dfs(self, curr, currWord: str, word: str, misMatch):
        if self.last:
            if len(word)>curr:
                tempM=0
                if word[curr] != self.char:
                    tempM=1
                
                total = misMatch + tempM + (len(word)-curr-1)
                if total<=maxMisMatch:
                    print(currWord+self.char)
            elif misMatch+1<=maxMisMatch:
                print(currWord+self.char)
            
    
        if misMatch>maxMisMatch:
            return
        if len(word)-1 < curr:
            for child in self.children:
                dfs(child, curr, currWord+self.char, word, misMatch+1)
            return
        match=0
        if word[curr] != root.char:
            match=1
    
        for child in root.children:
            dfs(child, curr+1, currWord+root.char, word, misMatch+match)
            dfs(child, curr, currWord+root.char, word, misMatch+match)
            
if __name__ == "__main__":
    root = TrieNode('*')
    root.add("aponkur")
    root.add("bnkur")
    maxMisMatch = 2
    for child in root.children:
        dfs(child,0,"", "cnkur", 0)
        
    # print(search(root, "ankur"))
    # print(search(root,"nothing"))

# rosalind_24_REVP
#
# Locating Restriction Sites
# https://rosalind.info/problems/revp/
#
# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

#0) using two pointer
#1) DNA string 생성 
#2) 짝수 window로 시작. 
#3) 2개씩 뻗어가며 C-G / A-T 조합 찾기
#4) 찾으면 index를 하나씩 넓혀가며 panlinedrom 찾기
#5) start index 찾기
#5) size는 4이상 12이하

complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def find_palindrome(DNA: str):
    
    palindrome = set()
      
    for i in range(len(DNA)-1):   
        #start from length of 2
        left, right = i, i+1
        while left >= 0 and right < len(DNA) and (right-left < 12):
            if complement_dict[DNA[left]] != DNA[right]: #not palindrome
                break
            elif 4 <= (right - left + 1) <= 12: #palindrome and length is 4~12
                palindrome.add((left+1, right-left+1))  #position, length
            left -= 1
            right += 1
                
    return palindrome
    
if __name__ == '__main__':
    
    with open('./datasets/rosalind_revp.txt') as inFile:
        
        DNA = ''.join(line.strip() for line in inFile.readlines()[1:])
        
    with open('./answers/rosalind_revp_outFile2.txt', 'w') as outFile:
        
        palindrome_list = find_palindrome(DNA)
        for pos, len in palindrome_list:
            print(f'{pos} {len}', file = outFile)

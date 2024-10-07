def decode_message( s: str, p: str) -> bool:

        if is_match(s, p):
                return True
        else:
                return False


def is_match(message, pattern):
    m = len(message)
    p = len(pattern)
    dp = [[False] * (p + 1) for _ in range(m + 1)]
    
    dp[0][0] = True  
    
    
    for j in range(1, p + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][p]



"highlight Functions
syn match cFunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>[^()]*)("me=e-2
syn match cFunctions "\<[a-zA-Z_][a-zA-Z_0-9]*\>\s*("me=e-1
hi cFunctions gui=NONE   ctermfg=blue



"========================================================
" Highlight All Math Operator
"========================================================
" C math operators
syn match       cMathOperator     display "[-+/*/%=]"
" C pointer operators
syn match       cPointerOperator  display "->/|/."
" C logical   operators - boolean results
syn match       cLogicalOperator  display "[!<>]=/="
syn match       cLogicalOperator  display "=="
" C bit operators
syn match       cBinaryOperator   display "/(&/||/|/^/|<</|>>/)=/="
" More C logical operators - highlight in preference to binary
syn match       cLogicalOperator  display "&&/|||"
syn match       cLogicalOperatorError display "/(&&/|||/)="

" Math Operator
hi cMathOperator            guifg=#3EFFE2
hi cPointerOperator         guifg=#3EFFE2
hi cLogicalOperator         guifg=#3EFFE2
hi cBinaryOperator          guifg=#3EFFE2
hi cBinaryOperatorError     guifg=#3EFFE2
hi cLogicalOperator         guifg=#3EFFE2
hi cLogicalOperatorError    guifg=#3EFFE2

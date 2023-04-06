def nhap():
    mcp=int(input("Nhap so muong ca phe:"))
    return mcp
def quydoi(mcp):
    mc=mcp//3
    mcp=mcp%3
    c=mc//16
    mc=mc%16
    print(c,"coc",mc,"muong canh",mcp,"muong ca phe")
mc=nhap()
quydoi(mc)
    


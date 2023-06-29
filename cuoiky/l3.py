#st.upper(),lower(): viết hoa hoặc viết thường
#st.isupper(),islower(): True False có đc viết hoa hay viết thường toàn xâu

#st.isalpha():True:ký tự chữ cái và k có ký tự trắng
#st.isnumeric(),isdecimal(): True: ký tự số, k trắng
#st.isalmun():True:chữ cái, số, k trắng
#st.isspace()True: trắng hoặc tab, dấu ngắt dòng
#st.istitle():các từ, mỗi từ dc viết thường và viết hoa chữ cái đầu

#st.startswith(str),endwith(str) True:chuỗi bắt đầu/kthuc bằng str

#st.join(ListOfString): ListOfString là list gồm chuỗi ký tự .join() dùng để nối các phần tử trong LOS = chuỗi t ứng
#', '.join(['cat','rats','bats'])
#->cat, rats, bats

#st.split(): tách
#'My name is Anh'.split()
#->['My', 'name', 'is', 'Anh']

#st.rjust(n,ch),ljust,center: trả về 1 chuỗi mới khi thêm vào gốc các ký tự ch
# sao cho chiều dài chuỗi bằng n và chuỗi gốc dc đặt bên phải, trái..

#st.strip(str),rstrip,lstrip:trả về chuỗi mới đã xoá các ký tự

#st.find(str,n):tìm chuỗi str trong gốc,tìm ký tự có số chỉ mục n
#trả về vị trí bắt đầu tìm thấy, nếu k có -1
#st.replace(oilvalue,newvalue,n)tìm, thay thế các chuỗi old xuất hiện gốc = new,với n lần tìm và thay thế

#st.re.search('[a-z]'.st) ktra các ký tự có chứa [a-z]k. lệnh import.re
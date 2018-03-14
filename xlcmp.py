import xlrd
import xlwt

class XlCmp():
    def __init__(self,file1,file2):
        self.file_1=file1#校验文件
        self.file_2=file2#基准文件
        self.same=True
        self.diff={}
        self.open_xls()

    def open_xls(self):
        f1=xlrd.open_workbook(self.file_1)
        f2=xlrd.open_workbook(self.file_2)
        f3=xlwt.Workbook()

        nsheets_1=f1.nsheets
        nsheets_2=f2.nsheets
        # if nsheets_1!=nsheets_2:raise EOFError#后续要在前面捕获异常，并表示两个EXCEL含sheet数量不一致
        for i in range(nsheets_2):
            sheet_1=f1.sheet_by_index(i)
            sheet_2=f2.sheet_by_index(i)
            for j in range(sheet_2.nrows):
                row_1=sheet_1.row_values(j)
                rows_2=sheet_2.row_values(j)
                if row_1==rows_2:continue
                for k in range(len(rows_2)):
                    if rows_2[k]!=row_1[k]:
                        l=rows_2[k]
                        self.save_location(sheet_2.name,j,k,l)


    def save_location(self,i,j,k,l):
        '''
        i代表sheet，j代表行数，k代表列数,l代表基准文件的内容
        '''
        self.same=False
        temp=self.diff.get(i,[])
        temp.append((j,k,l))
        self.diff[i]=temp


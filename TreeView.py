# Create hiracchical treeview Application
from tkinter import *
from tkinter import ttk


def Treeview_ImageProcess(tree_frame):
    # Tree scroll
    tree_Scroll = Scrollbar(tree_frame)
    tree_Scroll.pack(side=RIGHT, fill=Y)

    treeview = ttk.Treeview(
        tree_frame, yscrollcommand=tree_Scroll.set, selectmode="browse", height=20)
    treeview.pack()

    tree_Scroll.config(command=treeview.yview)

    treeview.column("#0", width=250, minwidth=25)
    treeview.heading("#0", text="Cải thiện và nâng cấp ảnh")
    # Treeview items
    treeview.insert(parent='', index='0', iid='item1',
                    text='Toán tử trên điểm ảnh')
    treeview.insert('item1', 'end', 'Image negative', text='Ảnh âm bản')
    treeview.insert('item1', 'end', 'Image Gray', text='Xám ảnh')
    treeview.insert('item1', 'end', 'Image reverse', text='Đảo ảnh')
    treeview.insert('item1', 'end', 'Logarithmic Tran',
                    text='Biến đổi sử dụng hàm log')
    treeview.insert('item1', 'end', 'Image Gamma',
                    text='Biến đổi sử dụng hàm mũ')
    treeview.insert('item1', 'end', 'Image Thresholding', text='Cắt theo mức')
    treeview.insert('item1', 'end', 'Histogram equal',
                    text='Cân bằng Histogram')

    treeview.insert(parent='', index='1', iid='item2',
                    text='Bộ lọc làm mịn và khôi phục ảnh')
    treeview.insert(
        'item2', 'end', 'Normalized Box Filter', text='Lọc trung bình')
    treeview.insert('item2', 'end', 'Gaussian Filter', text='Lọc Gauss')
    treeview.insert('item2', 'end', 'Median filter', text='Lọc trung vị')
    treeview.insert('item2', 'end', 'loclytuong', text='Lọc lý tưởng')
    treeview.insert('item2', 'end', 'Butterworth filter',
                    text='Lọc Butterworth')
    treeview.insert('item2', 'end', 'Gaussian filter', text='Lọc Gaussian')

    treeview.insert(parent='', index='end', iid='item3',
                    text='Bộ lọc nổi biên ảnh')
    treeview.insert('item3', 'end', 'Laplacian filter', text='Lọc Laplacian')
    treeview.insert('item3', 'end', 'Sobel filter', text='Lọc Sobel')

    treeview.insert(parent='', index='end', iid='item4', text='Nâng cấp ảnh')
    treeview.insert('item4', 'end', 'LoG', text='Laplacian of Gaussian')
    treeview.insert('item4', 'end', 'DoG', text='Difference of Gaussian')
    treeview.insert('item4', 'end', 'low pass filter', text='Lọc thông thấp')
    treeview.insert('item4', 'end', 'high pass filter', text='Lọc thông cao')

import pandas as pd

class FileSystem:
    def __init__(self) -> None:
        self.files=[]
        self.file_df=pd.DataFrame()

    def add_file(self, file_name=str, size=int, collection=''):
        self.files.append({
            'name': file_name,
            'size': size,
            'collection':collection
        })
        self.file_df=pd.DataFrame(self.files)
        return self.files
    def total_size(self):
        return self.file_df['size'].sum()
    def top_n_collections(self, n):
        filter_collesction=self.file_df[self.file_df['collection']!='']
        top_n= filter_collesction.groupby(['collection']).agg(total_size=('size','sum'))
        return top_n.sort_values(by='total_size', ascending=False).head(n)
    def generatereport(self,n):
        total_size=self.total_size()
        top_n_collection=self.top_n_collections(n)
        report = f"Total size of all files: {str(total_size) }\n" 
        report += f"Top {n} collections by file size:\n"
        report += f"{top_n_collection.head()}"
        return report

    


fs=FileSystem()    
# Add files to the system
fs.add_file("file1.txt", 100)
fs.add_file("file2.txt", 200, "collection1")
fs.add_file("file3.txt", 200, "collection1")
fs.add_file("file4.txt", 300, "collection2")
fs.add_file("file5.txt", 10)
print(fs.generatereport(2))

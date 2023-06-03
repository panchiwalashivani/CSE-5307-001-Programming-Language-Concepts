/**
Name        :   Shivani Panchiwala
UTA ID      :   1001982478
Version     :   Dev C++ 5.11
OS          :   Windows 11
 */

#include<stdio.h>
#include<iostream>
#include<dirent.h>
#include<sys/stat.h>
#include<string>
#include <unistd.h>
#define Get_Curr_Dir getcwd


// Returns the path of current working directory (CWD)
std::string get_cwd(void) {
  char buff[FILENAME_MAX];
  Get_Curr_Dir( buff, FILENAME_MAX );
  std::string current_working_dir(buff);
  return current_working_dir;
}

int get_Total_Size(char path[])
{
  int totalSize = 0;
  char filePath[2000];
  // fetches the current working directory (CWD)
  std::string cwd = get_cwd();
  struct dirent *item;
  struct stat file;

  // if path is empty then it will use the CWD
 if (strcmp(path, "") == 0){
    path = const_cast<char*>(cwd.c_str());
 }

  DIR *directory = opendir(path); // opens directory stream

  while ((item=readdir(directory))!=NULL) 
  {
    // "." is a hardlink to its containing directory. Hence, skipped.
    // ".." means parent directory. Hence, skipped.
    if(strcmp(item->d_name,".")==0 || strcmp(item->d_name,"..")==0)
    {
      continue;
    }
    strcpy(filePath,path);
    strcat(filePath,"/");
    strcat(filePath,item->d_name); // creating full path for item
    stat(filePath,&file);
    
    if(S_ISREG(file.st_mode))
    {
      FILE *start = fopen(filePath,"r");
      fseek(start,0L,SEEK_END);
      int value = ftell(start);
      totalSize += value;
      fclose(start);
    }
    else if (S_ISDIR(file.st_mode))
    {
      totalSize += get_Total_Size(filePath); // recursion call
    }
    else {
        printf("Neither a file nor a directory");
    }
  }
  return totalSize;

}

int main()
{
  int totalSize = get_Total_Size("");
  printf("\n******************");
  printf("\n Total size = %d Bytes",totalSize);
  printf("\n******************");

  return 0;
}

/**
Code Explanation
----------------
If no path is mentioned then the current directory is explored for its contents.
If the item is a file then its size is stored and if it is directory the same function is called with the directory's path.
This recursion stops when all directories have been explored and file sizes stored.
The final size is returned.
 */


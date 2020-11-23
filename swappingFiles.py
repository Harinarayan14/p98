def swap():
    print("Swap Files")
    file1 = input("Enter Name of File 1 ");
    file2 = input("Enter Name of File 2 ");
    data1 = open(file1);
    text1 = data1.read();
    data2 = open(file2);
    text2 = data2.read();
    wdata1 = open(file1,"w");
    wdata1.write(text2);
    wdata2 = open(file2,"w");
    wdata2.write(text1);
    print("Successfully Swapped");
swap();
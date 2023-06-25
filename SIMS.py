"""
Về sản phẩm:
1. pcode (string) mã các loại hàng hóa. Đây sẽ là khóa của cây và nó cần phải là độc nhất
2. pro_name (string) tên của các loại hàng hóa
3. quantity (integer) số lượng sản phẩm đi cùng với từng mã sản phẩm vào thời điểm đầu của mỗi ngày
4. saled (integer) số lượng hàng hóa đi cùng với từng mã sản phẩm được bán trong ngày (saled < quantity)
5. price (double) Giá của sản phẩm

Về khách hàng:
1. ccode (string) mã khách hàng (là duy nhất)
2. cus_name (string) tên của khách hàng
3. phone (string) số điện thoại của khách hàng (chỉ được chứa các chữ số)

Về việc đặt hàng:
1. pcode (string) mã sản phẩm đã được đặt
2. ccode (string) mã khách hàng đặt hàng
3. quantity (integer) số lượng đặt
"""

"""
Công việc:
1. BST: Dữ liệu của các sản phẩm
2. LinkedList: Dữ liệu của các khách hàng
3. LinkedList: Dữ liệu của việc đặt hàng
4. Báo cáo sản phẩm nhập
5. Truy vấn hàng tồn kho
6. Dữ liệu của việc bán hàng
7. Trình ghi việc mua, bán
"""

"""
Menu:
1.1 tải dữ liệu đã lưu
1.2 Nhập dữ liệu
1.3 In ra theo thuật toán inorder
1.4 In ra theo thuật toán breath-first
1.5 chuyển 1.3 vào file theo inorder
1.6 tìm kiếm theo mã sản phẩm
1.7 Xóa theo mã sản phẩm bằng cách copy
1.8 Cân bằng đơn giản 
1.9 Đếm số lượng của sản phẩm

2.1 Tải dữ liệu từ file
2.2 Thêm dữ liệu khách hàng vào cuối
2.3 Hiển thị dữ liệu
2.4 Chuyển dữ liệu khách hàng vào file
2.5 Tìm kiếm theo ccode
2.6 Xóa theo ccode

3.1 Nhập dữ liệu
3.2 hiển thị dữ liệu đặt hàng
3.3 Sắp xếp theo pcode và ccode

4.1 Sửa chi tiết sản phẩm
4.2 Thêm số lượng vào sản phẩm sẵn có
4.3 Xóa những sản phẩm mà đã hết hàng
4.4 Tìm sản phẩm theo mô tả sản phẩm

5.1 Đọc tất cả trong bảng và hiển thị trên cửa sổ Tkinter

6.1 Tạo ra một lượt bán mới
6.2 Xác định nhân viên có doanh số cao nhất
6.3 Xác định sản phẩm bán nhiều nhất

7.1 Kiểm tra tiến trình bán của
"""
import os

class Product:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode = pcode
        self.pro_name = pro_name
        self.quantity = quantity
        self.saled = saled
        self.price = price

    def __str__(self):
        return f"{self.pcode}\t{self.pro_name}\t{self.quantity}\t{self.saled}\t{self.price}"


class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def is_pcode_unique(self, pcode):
        return self._is_pcode_unique_helper(self.root, pcode)

    def _is_pcode_unique_helper(self, node, pcode):
        if node is None:
            return True

        if pcode == node.product.pcode:
            return False

        if pcode < node.product.pcode:
            return self._is_pcode_unique_helper(node.left, pcode)
        else:
            return self._is_pcode_unique_helper(node.right, pcode)

    def load_data_from_file(self):
        filename = "data.txt"  # Thay đổi tên tệp tin tại đây
        file_path = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines[1:]:
                    data = line.strip().split()
                    pcode = data[0]
                    pro_name = data[1]
                    quantity = int(data[2])
                    saled = int(data[3])
                    price = float(data[4])
                    product = Product(pcode, pro_name, quantity, saled, price)
                    self.insert(product)
                print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def input_and_insert_data(self):
        num_products = int(input("Enter the number of products: "))
        for _ in range(num_products):
            pcode = input("Enter product code: ")
            if not self.is_pcode_unique(pcode):
                print("Product pcode already exists. Please enter a unique product pcode.")
                continue

            pro_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            saled = int(input("Enter saled: "))
            price = float(input("Enter price: "))
            product = Product(pcode, pro_name, quantity, saled, price)
            self.insert(product)
            self.append_to_file(product)
            print("Product inserted successfully.")



    def insert(self, product):
        if self.root is None:
            self.root = Node(product)
        else:
            self._insert_rec(self.root, product)

    def _insert_rec(self, node, product):
        if product.pcode < node.product.pcode:
            if node.left is None:
                node.left = Node(product)
            else:
                self._insert_rec(node.left, product)
        elif product.pcode > node.product.pcode:
            if node.right is None:
                node.right = Node(product)
            else:
                self._insert_rec(node.right, product)
        else:
            return False

    def append_to_file(self, product):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, "a") as file:
            file.write(str(product) + "\n")


    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, root):
        if root is not None:
            self._in_order_traversal(root.left)
            print(f"Product Code: {root.product.pcode}")
            print(f"Product Name: {root.product.pro_name}")
            print(f"Quantity: {root.product.quantity}")
            print(f"Saled: {root.product.saled}")
            print(f"Price: {root.product.price}")
            print("--------------------")
            self._in_order_traversal(root.right)


    def breadth_first_traversal(self):
        if self.root is None:
            print("BST is empty.")
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(f"Product Code: {node.product.pcode}")
            print(f"Product Name: {node.product.pro_name}")
            print(f"Quantity: {node.product.quantity}")
            print(f"Saled: {node.product.saled}")
            print(f"Price: {node.product.price}")
            print("--------------------")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    def search_by_pcode(self, pcode):
        product = self._search_by_pcode(self.root, pcode)
        if product is not None:
            print(f"Product Code: {product.pcode}")
            print(f"Product Name: {product.pro_name}")
            print(f"Quantity: {product.quantity}")
            print(f"Saled: {product.saled}")
            print(f"Price: {product.price}")
        else:
            print("Product does not exist.")

    def _search_by_pcode(self, root, pcode):
        if root is None or root.product.pcode == pcode:
            return root.product
        if pcode < root.product.pcode:
            return self._search_by_pcode(root.left, pcode)
        return self._search_by_pcode(root.right, pcode)

    def delete_by_pcode(self, pcode):
        self.root = self._delete_by_pcode(self.root, pcode)
        self.save_data_to_file()  # Ghi lại dữ liệu sau khi xóa

    def _delete_by_pcode(self, root, pcode):
        if root is None:
            return root
        if pcode < root.product.pcode:
            root.left = self._delete_by_pcode(root.left, pcode)
        elif pcode > root.product.pcode:
            root.right = self._delete_by_pcode(root.right, pcode)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._find_min(root.right)
            root.product.pcode = temp.product.pcode
            root.product.pro_name = temp.product.pro_name
            root.product.quantity = temp.product.quantity
            root.product.saled = temp.product.saled
            root.product.price = temp.product.price
            root.right = self._delete_by_pcode(root.right, temp.product.pcode)
        return root

    def save_data_to_file(self):
        filename = "data.txt"
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, "w") as file:
            self._in_order_traversal_and_save(self.root, file)


    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal_to_file(self):
        filename = "data.txt"
        with open(filename, 'w') as file:
            self._in_order_traversal_and_save(self.root, file)

    def _in_order_traversal_and_save(self, root, file):
        if root is not None:
            self._in_order_traversal_and_save(root.left, file)
            file.write(f"Product Code: {root.product.pcode}\n")
            file.write(f"Product Name: {root.product.pro_name}\n")
            file.write(f"Quantity: {root.product.quantity}\n")
            file.write(f"Saled: {root.product.saled}\n")
            file.write(f"Price: {root.product.price}\n")
            file.write("--------------------\n")
            self._in_order_traversal_and_save(root.right, file)

    def simply_balance(self):
        nodes = []
        self._store_nodes_inorder(self.root, nodes)
        n = len(nodes)
        return self._build_balanced_tree(nodes, 0, n - 1)

    def _store_nodes_inorder(self, root, nodes):
        if root is not None:
            self._store_nodes_inorder(root.left, nodes)
            nodes.append(root)
            self._store_nodes_inorder(root.right, nodes)

    def _build_balanced_tree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self._build_balanced_tree(nodes, start, mid - 1)
        node.right = self._build_balanced_tree(nodes, mid + 1, end)
        return node


    def count_products(self):
        return self._count_products_rec(self.root)

    def _count_products_rec(self, root):
        if root is None:
            return 0
        return 1 + self._count_products_rec(root.left) + self._count_products_rec(root.right)
    

class Customer:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
        self.next = None

class CustomerList:
    def __init__(self):
        self.head = None
        self.filename = "customer.txt"
        self.ccode_set = set()

    def load_data_from_file(self):
        file_path = os.path.join(os.path.dirname(__file__), self.filename)

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3:
                        ccode = data[0]
                        cus_name = data[1]
                        phone = data[2]
                        customer = Customer(ccode, cus_name, phone)
                        self.append(customer)
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def append(self, customer):
        if customer.ccode in self.ccode_set:
            print("Customer code already exists. Unable to add customer.")
            return

        if self.head is None:
            self.head = customer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = customer

        self.ccode_set.add(customer.ccode)  # Thêm ccode vào set
        self.save_to_file(self.filename)  # Lưu khách hàng vào file customer.txt

    def display(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if not lines:
                    print("No customer data.")
                else:
                    for line in lines:
                        data = line.strip().split("\t")
                        if len(data) == 3:
                            ccode = data[0]
                            cus_name = data[1]
                            phone = data[2]
                            print(f"Customer Code: {ccode}")
                            print(f"Customer Name: {cus_name}")
                            print(f"Phone: {phone}")
                            print("--------------------")
        except FileNotFoundError:
            print("File not found.")

    def save_to_file(self, filename):
        file_path = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                current = self.head
                while current:
                    file.write(f"{current.ccode}\t{current.cus_name}\t{current.phone}\n")
                    current = current.next
                print("Customer list saved to file successfully.")
        except FileNotFoundError:
            print("File not found.")

    def search_by_ccode(self, ccode):
        file_path = os.path.join(os.path.dirname(__file__), self.filename)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3 and data[0] == ccode:
                        cus_name = data[1]
                        phone = data[2]
                        print(f"Customer Code: {ccode}")
                        print(f"Customer Name: {cus_name}")
                        print(f"Phone: {phone}")
                        return
            print("Customer does not exist.")
        except FileNotFoundError:
            print("File not found.")

    def delete_by_ccode(self, ccode):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
            with open(self.filename, "w") as file:
                deleted = False
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) == 3 and data[0] != ccode:
                        file.write(line)
                    else:
                        deleted = True
                if deleted:
                    print("Customer deleted.")
                else:
                    print("Customer does not exist.")
        except FileNotFoundError:
            print("File not found.")

# order list
class Order:
    def __init__(self, pcode, ccode, quantity):
        self.pcode = str(pcode)
        self.ccode = str(ccode)
        self.quantity = quantity

class OrderList:
    def __init__(self):
        self.orders = []
    
    def input_order_data(self):
        num_orders = int(input("Enter the number of orders: "))
        for _ in range(num_orders):
            pcode = input("Enter product code: ")
            ccode = input("Enter customer code: ")
            quantity = int(input("Enter quantity: "))
            order = Order(pcode, ccode, quantity)
            self.orders.append(order)

    def display(self):
        if not self.orders:
            print("No orders to display.")
        else:
            for order in self.orders:
                print(f"Product Code: {order.pcode}")
                print(f"Customer Code: {order.ccode}")
                print(f"Quantity: {order.quantity}")
                print("--------------------")

    def sort_by_pcode(self):
        self.orders.sort(key=lambda x: x.pcode)

    def sort_by_ccode(self):
        self.orders.sort(key=lambda x: x.ccode)


# Menu
def display_menu():
    print("Sales and Inventory Management System (SIMS) Menu:")
    print("1 Products")
    print("2 Customer list")
    print("3 Order list")
    print("0. Exit")

# Main program
bst = BST()
customer_list = CustomerList()
order_list = OrderList()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("Products:")
            print("1.1 Load data from file")
            print("1.2 Input & insert data")
            print("1.3 In-order traversal")
            print("1.4 Breadth-first traversal")
            print("1.5 In-order traversal to file")
            print("1.6 Search by pcode")
            print("1.7 Delete by pcode by copying")
            print("1.8 Simply balancing")
            print("1.9 Count number of products")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "1.1":
                bst.load_data_from_file()
            elif sub_choice == "1.2":
                bst.input_and_insert_data()
            elif sub_choice == "1.3":
                bst.in_order_traversal()
            elif sub_choice == "1.4":
                bst.breadth_first_traversal()
            elif sub_choice == "1.5":
                bst.in_order_traversal_to_file()
            elif sub_choice == "1.6":
                pcode = input("Enter the product code: ")
                bst.search_by_pcode(pcode)
            elif sub_choice == "1.7":
                pcode = input("Enter the product code: ")
                bst.delete_by_pcode(pcode)
            elif sub_choice == "1.8":
                bst.simply_balance()
            elif sub_choice == "1.9":
                count = bst.count_products()
                print(f"Number of products: {count}")
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            # Sub-menu for Customer list
            print("Customer list:")
            print("2.1 Load data from file")
            print("2.2 Input & add to the end")
            print("2.3 Display data")
            print("2.4 Save customer list to file")
            print("2.5 Search by ccode")
            print("2.6 Delete by ccode")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "2.1":
                customer_list.load_data_from_file()
            elif sub_choice == "2.2":
                ccode = input("Enter customer code: ")
                cus_name = input("Enter customer name: ")
                phone = input("Enter phone number: ")
                customer = Customer(ccode, cus_name, phone)
                customer_list.append(customer)
            elif sub_choice == "2.3":
                customer_list.display()
            elif sub_choice == "2.4":
                filename = input("Enter the filename: ")
                customer_list.save_to_file(filename)
            elif sub_choice == "2.5":
                ccode = input("Enter the customer code: ")
                customer_list.search_by_ccode(ccode)
            elif sub_choice == "2.6":
                ccode = input("Enter the customer code: ")
                customer_list.delete_by_ccode(ccode)
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


    elif choice == "3":
        while True:
            # Sub-menu for Order list
            print("Order list:")
            print("3.1 Input order data")
            print("3.2 Display orders")
            print("3.3 Sort orders by product code")
            print("3.4 Sort orders by customer code")
            sub_choice = input("Enter your choice (Enter 0 to go back to main menu): ")

            if sub_choice == "3.1":
                order_list.input_order_data()
            elif sub_choice == "3.2":
                order_list.display()
            elif sub_choice == "3.3":
                order_list.sort_by_pcode()
                order_list.display()
            elif sub_choice == "3.4":
                order_list.sort_by_ccode()
                order_list.display()
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")



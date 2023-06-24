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
class Product:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode = pcode
        self.pro_name = pro_name
        self.quantity = quantity
        self.saled = saled
        self.price = price
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def input_and_insert_data(self):
        num_products = int(input("Enter the number of products: "))
        for _ in range(num_products):
            pcode = input("Enter product code: ")
            pro_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            saled = int(input("Enter saled: "))
            price = float(input("Enter price: "))
            product = Product(pcode, pro_name, quantity, saled, price)
            self.insert(product)

    def insert(self, product):
        self.root = self._insert_rec(self.root, product)

    def _insert_rec(self, root, product):
        if root is None:
            return product
        if product.pcode < root.pcode:
            root.left = self._insert_rec(root.left, product)
        elif product.pcode > root.pcode:
            root.right = self._insert_rec(root.right, product)
        return root

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, root):
        if root is not None:
            self._in_order_traversal(root.left)
            print(f"Product Code: {root.pcode}")
            print(f"Product Name: {root.pro_name}")
            print(f"Quantity: {root.quantity}")
            print(f"Saled: {root.saled}")
            print(f"Price: {root.price}")
            print("--------------------")
            self._in_order_traversal(root.right)

    def breadth_first_traversal(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(f"Product Code: {node.pcode}")
            print(f"Product Name: {node.pro_name}")
            print(f"Quantity: {node.quantity}")
            print(f"Price: {node.price}")
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
        if root is None or root.pcode == pcode:
            return root
        if pcode < root.pcode:
            return self._search_by_pcode(root.left, pcode)
        return self._search_by_pcode(root.right, pcode)

    def delete_by_pcode(self, pcode):
        self.root = self._delete_by_pcode(self.root, pcode)

    def _delete_by_pcode(self, root, pcode):
        if root is None:
            return root
        if pcode < root.pcode:
            root.left = self._delete_by_pcode(root.left, pcode)
        elif pcode > root.pcode:
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
            root.pcode = temp.pcode
            root.pro_name = temp.pro_name
            root.quantity = temp.quantity
            root.saled = temp.saled
            root.price = temp.price
            root.right = self._delete_by_pcode(root.right, temp.pcode)
        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal_and_save(self, filename):
        with open(filename, 'w') as file:
            self._in_order_traversal_and_save(self.root, file)

    def _in_order_traversal_and_save(self, root, file):
        if root is not None:
            self._in_order_traversal_and_save(root.left, file)
            file.write(f"Product Code: {root.pcode}\n")
            file.write(f"Product Name: {root.pro_name}\n")
            file.write(f"Quantity: {root.quantity}\n")
            file.write(f"Saled: {root.saled}\n")
            file.write(f"Price: {root.price}\n")
            file.write("--------------------\n")
            self._in_order_traversal_and_save(root.right, file)

    def balance_tree(self):
        nodes = self._store_in_order(self.root)
        self.root = self._build_balanced_tree(nodes, 0, len(nodes) - 1)

    def _store_in_order(self, root):
        nodes = []
        self._store_in_order_rec(root, nodes)
        return nodes

    def _store_in_order_rec(self, root, nodes):
        if root is not None:
            self._store_in_order_rec(root.left, nodes)
            nodes.append(root)
            self._store_in_order_rec(root.right, nodes)

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
    
    def append(self, customer):
        if self.head is None:
            self.head = customer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = customer

    def display(self):
        current = self.head
        while current:
            print(f"Customer Code: {current.ccode}")
            print(f"Customer Name: {current.cus_name}")
            print(f"Phone: {current.phone}")
            print("--------------------")
            current = current.next
    
    def search_by_ccode(self, ccode):
        current = self.head 
        while current:
            if current.ccode == ccode:
                print(f"Customer Code: {current.ccode}")
                print(f"Customer Name: {current.cus_name}")
                print(f"Phone: {current.phone}")
                return 
            current = current.next
        print("Customer does not exist.")

    def delete_by_ccode(self, ccode):
        if self.head is None:
            return
        if self.head.ccode == ccode:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.ccode == ccode:
                previous.next = current.next
                return
            previous = current
            current = current.next
        print("Customer does not exist.")

class Order:
    def __init__(self, pcode, ccode, quantity):
        self.pcode = pcode
        self.ccode = ccode
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
        for order in self.orders:
            print(f"Product Code: {order.pcode}")
            print(f"Customer Code: {order.ccode}")
            print(f"Quantity: {order.quantity}")
            print("--------------------")

    def sort_by_pcode(self):
        self.orders.sort(key=lambda x: x.pcode)

    def sort_by_ccode(self):
        self.orders.sort(key=lambda x: x.ccode)

def run_tests():
    # Test Product and BST classes
    bst = BST()

    # Test inserting products
    product1 = Product("P001", "Product 1", 10, 5, 9.99)
    product2 = Product("P002", "Product 2", 5, 2, 19.99)
    product3 = Product("P003", "Product 3", 8, 3, 14.99)

    bst.insert(product1)
    bst.insert(product2)
    bst.insert(product3)

    # Test in-order traversal
    print("In-order traversal:")
    bst.in_order_traversal()

    # Test breadth-first traversal
    print("Breadth-first traversal:")
    bst.breadth_first_traversal()

    # Test search for product by pcode
    print("Search for product by pcode:")
    bst.search_by_pcode("P002")

    # Test delete product by pcode
    print("Delete product by pcode:")
    bst.delete_by_pcode("P002")
    bst.in_order_traversal()

    # Test balance tree
    print("Balance tree:")
    bst.balance_tree()
    bst.in_order_traversal()

    # Test counting number of products
    print("Count number of products:", bst.count_products())

    # Test CustomerList class
    customer_list = CustomerList()

    # Test appending customers
    customer1 = Customer("C001", "Customer 1", "123456789")
    customer2 = Customer("C002", "Customer 2", "987654321")

    customer_list.append(customer1)
    customer_list.append(customer2)

    # Test display customer list
    print("Display customer list:")
    customer_list.display()

    # Test search for customer by ccode
    print("Search for customer by ccode:")
    customer_list.search_by_ccode("C001")

    # Test delete customer by ccode
    print("Delete customer by ccode:")
    customer_list.delete_by_ccode("C002")
    customer_list.display()

    # Test OrderList class
    order_list = OrderList()

    # Test input order data
    order1 = Order("P001", "C001", 3)
    order2 = Order("P002", "C002", 5)
    order3 = Order("P003", "C001", 2)

    order_list.orders.append(order1)
    order_list.orders.append(order2)
    order_list.orders.append(order3)

    # Test display order list
    print("Display order list:")
    order_list.display()

    # Test sorting order list by pcode
    print("Sort order list by pcode:")
    order_list.sort_by_pcode()
    order_list.display()

    # Test sorting order list by ccode
    print("Sort order list by ccode:")
    order_list.sort_by_ccode()
    order_list.display()


# Run the tests
run_tests()

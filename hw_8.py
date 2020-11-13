'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        self._iplist = ipList

    @property
    def ipList(self):
        return self._iplist

    @ipList.setter
    def ipList(self, newList):
        self._iplist = newList

    def reverse_IP(self):
        new_list = list()
        for ip in self._iplist:
            split_list = ip.split('.')

            reserved_list = split_list[::-1]
            reserved_ip = ".".join(reserved_list)
            new_list.append(reserved_ip)

            self._iplist = new_list

    def get_oct_1_3(self):
        new_list = list()
        for ip in self._iplist:
            split_list = ip.split('.')

            without_first_list = split_list[1:4]
            without_first_ip = ".".join(without_first_list)
            new_list.append(without_first_ip)

            self._iplist = new_list

    def get_oct_3(self):
        new_list = list()
        for ip in self._iplist:
            split_list = ip.split('.')
            last_octets_list = split_list[3:4]
            last_octets_ip = ".".join(last_octets_list)
            new_list.append(last_octets_ip)

            self._iplist = new_list


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

        #unit_name
        @property
        def unit_name(self):
            return self._unit_name

        @unit_name.setter
        def unit_name(self,value):
            self._unit_name = value

        #mac_address
        @property
        def mac_address(self):
            return self._mac_address

        @mac_address.setter
        def mac_address(self, value):
            self._mac_address = value

        #ip_address
        @property
        def ip_address(self):
            return self._ip_address

        @ip_address.setter
        def ip_address(self, value):
            self._ip_address = value

        #login
        @property
        def login(self):
            return self._login

        @login.setter
        def login(self, value):
            self._login = value

        #password
        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, value):
            self._password = value

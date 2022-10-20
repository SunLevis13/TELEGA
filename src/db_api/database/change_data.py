class Database:
    def __init__(self):
        self.item_data = [
            {
                'id': 63,
                'name': 'Редис',
                'description': 'Редис крупный',
                'count': 1
            },
            {
                'id': 84,
                'name': 'Помидоры',
                'description': 'Помидоры сливовидные',
                'count': 1
            },
            {
                'id': 47,
                'name': 'Кукуруза',
                'description': 'Кукуруза в початках',
                'count': 1
            }
        ]
    def add_item(self, id: int, name: str, description: str, count: int):
        self.item_data.append(
            {
                'id': id,
                'name': name,
                'description': description,
                'count': count
            }
        )
    def get_item(self, item_index):
        status = 'Ok'
        if item_index == 0:
            status = 'Small'
        elif item_index == len(self.item_data) - 1:
            status = 'Big'
        return status, self.item_data[item_index]


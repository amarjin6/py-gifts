from dotenv import load_dotenv
import os
from dependencies import singleton, transient


class Workers(transient.Transient):
    def __init__(self, techMaps: str):
        super().__init__()
        self.techMaps = techMaps

    def toDo(self):
        print(f'Order {self.techMaps} completed')
        self.techMaps = 'num876544567'


class Manufacture(transient.Transient):
    def __init__(self, item: str, workers: Workers):
        super().__init__()
        self.invoice = item
        self.workers = workers

    def produce(self):
        self.workers.toDo()
        print(f'Item {self.invoice} produced')
        self.invoice = 'axles'


class Service(singleton.Singleton):
    def __init__(self, manufacture: Manufacture):
        super().__init__()
        self.manufacture = manufacture

    def repair(self):
        self.manufacture.produce()
        print('Done!')


if __name__ == '__main__':
    load_dotenv()
    service = Service(Manufacture(item=os.getenv('item'), workers=Workers(techMaps=os.getenv('techMaps'))))
    service.repair()
    print(id(service))
    service2 = Service(Manufacture(item=os.getenv('item2'), workers=Workers(techMaps=os.getenv('techMaps2'))))
    service2.repair()
    print(id(service2))

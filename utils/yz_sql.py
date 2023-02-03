"""
Title Here

*******************
Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com
*******************

"""
import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


class YzSQL:
    def __init__(self, db_path: str):
        """create engine"""
        self.engine = create_engine(f'sqlite:///{db_path}', echo=False)
        print('Connect success')

    def save_data(self, data, table_name, **kwargs):
        """
        存储数据至sql
        :param data: 数据
        :param table_name: 存储数据表格名称
        :return:
        """
        data.to_sql(name=table_name, con=self.engine, **kwargs)

    def query(self, sql: object, **kwargs: object) -> object:
        return pd.read_sql(sql=sql, con=self.engine, **kwargs)

    def drop_table(self, table_name):
        base = declarative_base()
        metadata = MetaData()
        metadata.reflect(bind=self.engine)

        try:
            table = metadata.tables[table_name]
            if table is not None:
                base.metadata.drop_all(self.engine, [table], checkfirst=True)
        except KeyError:
            print(f'No table named {table_name}')

    def change_data_base(self, db_path: str):
        self.engine = create_engine(f'sqlite:///{db_path}', echo=False)

    def add_column(self, table_name, adding_column, index_name):
        data = self.query(sql=f"SELECT * FROM {table_name}", index_col=index_name)
        data = pd.concat([data, adding_column], axis=1, join='outer')

        self.save_data(data=data, table_name=table_name, method='replace')

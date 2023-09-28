# Test task AD PROFIT MEDIA LTD

## Installation

1. Clone repository:
    ```bash
    git clone https://github.com/YKonoplyov/lunch_system.git
    ```
2. Create a virtual environment:
    ```shell
   python -m venv venv
   ``` 
   and activate it:
   on windows
   ```shell
   venv\Scripts\activate 
   ```
   on macOS or Linux:
    ```bash
    source venv/bin/activate 
    ```
3. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Configure the application by setting environment variables:
   SECRET_KEY - secret key for django app, you can generate it [here](https://djecrety.ir/)

5. Apply migrations for database:
    ```shell
   python manage.py migrate
    ```
6. Start application:
    ```shell
    python manage.py runserver
    ```

## Endpoints:

### Spend app:

- [GET, POST] api/v1/spend/: retrieve list of SpendStatistic objects, create SpendStatistic object
- [GET, PUT, PATCH, DELETE] api/v1/spend/{id} : retrieve, update, delete specified SpendStatistic object
- [GET] api/v1/spend_statistic/: retrieve queryset of SpendStatistic objects grouped by **name** and **date** with sums of:\
  spend, impressions, clicks, conversion fields and sum of RevenueStatistic field revenue 

### Revenue app:

- [GET, POST] api/v1/revenue/: retrieve list of RevenueStatistic objects, create RevenueStatistic object
- [GET, PUT, PATCH, DELETE] api/v1/spend/{id} : retrieve, update, delete specified RevenueStatistic object
- [GET] api/v1/revenue_statistic/: retrieve queryset of RevenueStatistic objects grouped by **name** and **date** with sums of:\
  revenue field and sums of SpendStatistic fields spend, impressions, clicks, conversion fields.  
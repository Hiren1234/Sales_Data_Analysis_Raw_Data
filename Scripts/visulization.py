import matplotlib.pyplot as plt

def sales_chart(region_sales):
    region_sales.plot(kind='bar', x='Region', y='Sales', figsize=(15,10))
    plt.title('Sales By Region ')
    plt.xlabel('Region')
    plt.ylabel('Sales')
    plt.savefig("Outputs/Charts/Sales_By_Region.png")
    plt.show()

# Month_Wise_Revenue
#  def month_wise_revenue(total_revenue):
def year_chart(Year_wise_revenue):

    Year_wise_revenue.plot(kind='bar', x='Year', y='Sales', figsize=(15,10))
    plt.title('Sales By Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')


    plt.savefig("Outputs/Charts/Sales_by_Year.png")
    plt.show()

def monthly_sales_chart(month_wise_sales):
     month_wise_sales.plot(kind='line', x='Month', y='Sales', figsize=(15,10))
     plt.title('Sales By Month')
     plt.xlabel('Month')
     plt.ylabel('Sales')
     plt.savefig("Outputs/Charts/Sales_by_Month.png")
     plt.show()

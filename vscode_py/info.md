# covoid-2019说明
* pandas可视化肺炎数据基本操作
  * drop_duplicates去重
  * groupby定位分组
  * get_group选定分组
  * tolist转为列表
* 函数定义
  * 默认值预设，```item_name='Cumulative_cases'```
* 画图
  * 线型属性赋值，```plt.plot(time,china_cases,'-.',color='red',label='China')```
  xdata ydata,线性、颜色、legend label name
  * 其它
    ```
        plt.grid(axis='both')


    ax=plt.gca()#坐标句柄
    ax.set_facecolor('#FFFAF0') #背景颜色

    #调整x刻度，相隔x刻度显示1个，防止过多显示
    x=30
    ax.xaxis.set_major_locator(ticker.MultipleLocator(x))   
    plt.xticks(rotation=60) #旋转x坐标时间标记，防止xlabel太长重合

    plt.legend()
    plt.tight_layout()    #自动调整
    plt.show()
    ```
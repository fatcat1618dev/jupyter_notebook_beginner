# covoid-2019˵��
* pandas���ӻ��������ݻ�������
  * drop_duplicatesȥ��
  * groupby��λ����
  * get_groupѡ������
  * tolistתΪ�б�
* ��������
  * Ĭ��ֵԤ�裬```item_name='Cumulative_cases'```
* ��ͼ
  * �������Ը�ֵ��```plt.plot(time,china_cases,'-.',color='red',label='China')```
  xdata ydata,���ԡ���ɫ��legend label name
  * ����
    ```
        plt.grid(axis='both')


    ax=plt.gca()#������
    ax.set_facecolor('#FFFAF0') #������ɫ

    #����x�̶ȣ����x�̶���ʾ1������ֹ������ʾ
    x=30
    ax.xaxis.set_major_locator(ticker.MultipleLocator(x))   
    plt.xticks(rotation=60) #��תx����ʱ���ǣ���ֹxlabel̫���غ�

    plt.legend()
    plt.tight_layout()    #�Զ�����
    plt.show()
    ```
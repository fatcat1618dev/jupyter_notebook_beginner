function y=myplot(method,x)
    y=method(x);
    plot(x,y,'p-')
    xlabel('X')
    ylabel('Y')
    title('Plot-Func')
    grid on
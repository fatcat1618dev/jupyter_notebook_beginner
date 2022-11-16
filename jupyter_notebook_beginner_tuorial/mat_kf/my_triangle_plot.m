function y=my_triangle_plot(x)
    y=sin(x);
    plot(x,y,'p-')
    xlabel('X')
    ylabel('Y')
    title('Triangle-Func')
    grid on
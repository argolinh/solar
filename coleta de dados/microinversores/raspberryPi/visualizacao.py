import matplotlib.pyplot as plt
import matplotlib.animation as animation 

fig, (ax1, ax2 ) = plt.subplots(2, 1)

def animate(i):
    data = pd.read_csv('dados_painel.csv')
    ax1.clear()
    ax2.clear()
    
    ax1.plot(data['Timestamp'], data['Irradiancia'])
    ax1.set_title('Irradiância Solar')
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Irradiância (w/m^2)')

    ax2.plot(data['Timestamp'], data ['Irradiância Solar'])
    ax2.set_Ttitle('Temperatura')
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Temperatura (°C)')

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

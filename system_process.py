import psutil


def about_commands():
    """
    Displays a menu of options for checking various system metrics.

    This function provides a user-friendly interface for accessing information
    about the system's CPU, memory, hardware, and network.

    Returns:
        None
    """

    print("Related to CPU:")
    print("Enter the 'check cpu process' for check CPU process\n Enter 'check cpu cores' for check CPU cores\n Enter 'check cpu stats' for check CPU statistics\n Enter 'check cpu usage' for check CPU usage\n Enter 'check cpu time' for check how many time CPU was used by process\n Enter 'check cpu frequency' for check CPU frequency\n ")
    print()

    print("Related to Memory:")
    print("Enter the 'check memory stats' for check virtual memory full stats\n Enter the 'check swap memmory' for get full swap memory stats\n Enter the 'memory process' for check memory process")
    print()

    print("Related to other hardware:")
    print("Enter the 'check hardware temp' for check hardware temperature\n Enter the 'check battery information' for check battery information\n Enter the 'check fan speed' for check your system fan speed\n Enter the 'check boot time' for check your system boot time")
    print()

    print("Related to networks: ")
    print("Enter the 'check network stats' for networks stats as per your network")


def check_cpu_process():
    cpu_percentages = psutil.cpu_percent(percpu=True)
    print("Here is your system's CPU process usage per core:")
    for i, perc in enumerate(cpu_percentages):
        print(f"Core {i}: {perc}%")


def check_cpu_cores():
    cores = psutil.cpu_count(logical=False)
    print(f"Here is the number of physical CPU cores: {cores}")


def check_cpu_stats():
    stats = psutil.cpu_stats()
    print("Here are your CPU stats:")
    print(f"  Context switches: {stats.ctx_switches}")
    print(f"  Interrupts: {stats.interrupts}")
    print(f"  Soft interrupts: {stats.soft_interrupts}")
    print(f"  Syscalls: {stats.syscalls}")


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Here is your current CPU usage: {cpu_usage}%")


def check_cpu_time():
    times = psutil.cpu_times()
    print("Here is your CPU time:")
    print(f"  User: {times.user} seconds")
    print(f"  System: {times.system} seconds")
    print(f"  Idle: {times.idle} seconds")
    if hasattr(times, 'iowait'):
        print(f"  IOWait: {times.iowait} seconds")


def check_cpu_frequency():
    freq = psutil.cpu_freq()
    print("Here is your CPU frequency:")
    print(f"  Current: {freq.current:.2f} MHz")
    print(f"  Min: {freq.min:.2f} MHz")
    print(f"  Max: {freq.max:.2f} MHz")


def check_memory_stats():
    vm = psutil.virtual_memory()
    print("Here is your virtual memory stats:")
    print(f"  Total: {vm.total} bytes")
    print(f"  Available: {vm.available} bytes")
    print(f"  Used: {vm.used} bytes")
    print(f"  Percentage: {vm.percent}%")


def check_swap_memory():
    swap = psutil.swap_memory()
    print("Here is your swap memory stats:")
    print(f"  Total swap: {swap.total} bytes")
    print(f"  Used swap: {swap.used} bytes")
    print(f"  Free swap: {swap.free} bytes")
    print(f"  Percentage: {swap.percent}%")


def check_memory_process():
    p = psutil.Process()
    mem_info = p.memory_info()
    print(f"RSS: {mem_info.rss} bytes")
    print(f"VMS: {mem_info.vms} bytes")


def check_hardware_temp():
    temps = psutil.sensors_temperatures()
    print("Here is your hardware temperature:")
    for name, entries in temps.items():
        print(f"  {name}:")
        for entry in entries:
            print(f"    {entry.label or 'Unnamed'}: {entry.current}°C")


def check_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        print(f"Here is your battery information:")
        print(f"  Battery percent: {battery.percent}%")
        print(f"  Time left: {battery.secsleft} seconds")
        print(f"  Power plugged in: {
              'Yes' if battery.power_plugged else 'No'}")
    else:
        print("No battery information available.")


def check_fan_speed():
    fans = psutil.sensors_fans()
    print("Here is your fan speed:")
    for name, entries in fans.items():
        print(f"  {name}:")
        for entry in entries:
            print(f"    {entry.label or 'Unnamed'}: {entry.current} RPM")


def check_boot_time():
    boot_time = psutil.boot_time()
    print(f"Here is your system boot time: {boot_time}")


def check_network_stats():
    net = psutil.net_io_counters()
    print("Here is your network stats:")
    print(f"  Bytes sent: {net.bytes_sent}")
    print(f"  Bytes received: {net.bytes_recv}")
    print(f"  Packets sent: {net.packets_sent}")
    print(f"  Packets received: {net.packets_recv}")
    print(f"  Errors in sending: {net.errin}")
    print(f"  Errors in receiving: {net.errout}")
    print(f"  Drops in sending: {net.dropin}")
    print(f"  Drops in receiving: {net.dropout}")


def check():
    """
    Continuously prompts the user to input a command to check various system metrics.
    """
    while True:
        try:
            check_input = input(
                "What do you want to check about your system? Write the command here: ").lower().strip()

            if check_input == 'check cpu process':
                check_cpu_process()
            elif check_input == 'check cpu cores':
                check_cpu_cores()
            elif check_input == 'check cpu stats':
                check_cpu_stats()
            elif check_input == 'check cpu usage':
                check_cpu_usage()
            elif check_input == 'check cpu time':
                check_cpu_time()
            elif check_input == 'check cpu frequency':
                check_cpu_frequency()
            elif check_input == 'check memory stats':
                check_memory_stats()
            elif check_input == 'check swap memory':
                check_swap_memory()
            elif check_input == 'check memory process':
                check_memory_process()
            elif check_input == 'check hardware temp':
                check_hardware_temp()
            elif check_input == 'check battery information':
                check_battery_info()
            elif check_input == 'check fan speed':
                check_fan_speed()
            elif check_input == 'check boot time':
                check_boot_time()
            elif check_input == 'check network stats':
                check_network_stats()
            else:
                print("Invalid input. Please try again.")

        except Exception as e:
            print(e)


def main():
    about_commands()
    check()


if __name__ == "__main__":
    main()

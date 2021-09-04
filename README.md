# Videogame Limiter
Limit the amount of time you spend playing video games. Configure maximum time spent in a week or by day. Useful for video games that don't have a natural breakpoint (i.e. Factorio).

## Interface

### Limit setter

Limits can be set as a maximum number of hours player per week or maximum hours played by day. This could allow, for example, 6 hours in a week, or 2 hours a schoolnight/worknight and 4 hours each weekend day.

### Limit enforcer

Limits can be viewed by opening the Videogame Limiter and viewing the hours consumed vs. available

Limits will have translucent reminder pop-over screens that appear N minutes before the limit will be enforce. These reminders can be used to snooze the limit M times for L minutes before snoozing is disabled. These reminders will contain a countdown with the number of minutes:seconds left.

When the limit is reached the program will be closed.

## Videogame service

### Steam
The program can determine if Steam is currently running by reading the value of HKEY_CURRENT_USER\Software\Valve\Steam in the Windows Registry.

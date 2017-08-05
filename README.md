# debt-balancer

debt-balancer is a command line tool for determing who owes someone how much money to balance out a shared cost. I built this as a tool for me for sharing the cost of vacations with friends.

This project isn't polished, but it works for me.

## Quick Example

Assume a trip with 5 people. Some people paid for groceries and others paid for misc items. The total amount paid per person towards shared expenses are as follows.

* Joel paid $0
* Ben paid $102.14
* John paid $1465.83
* Luke paid $554.51
* Peter paid $32.50

And we want a net result that everyone paid the same amount you'd run the command:

```shell
luke@luke-laptop:~/projects/debt-balance$ python3 runner.py --names "Joel,Ben,John,Luke,Peter" --paid "0,102.14,1465.83,554.51,32.50"
```

Which would return:

```shell
Amount everyone should have paid total: 431.00

Ben should pay Luke $123.51
Ben should pay John $205.34
Peter should pay John $398.50
Joel should pay John $431.00
```

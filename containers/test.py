from prettytable import PrettyTable

new_table = PrettyTable()
new_table.add_column('lxc04 containers',['dns1','dr1','kaf1','grafana','releases','sentinel1','-'])

new_table.add_column('lxc05 containers',['af1','dns2','dr2','kaf2','-','-','-'])
new_table.add_column('lxc06 containers',['app1','lb1','dr3','sentinel2','zabbix','-','-'])
new_table.add_column('lxc07 containers',['af2','app2','dr4','jn1','jtrans','lb2','-'])
new_table.add_column('lxc08 containers',['app3','dr5','drzoo3','influxdb','jn2','redis1','zoo2'])
new_table.add_column('lxc09 containers',['app4','dr6','drzoo1','nm1','redis2','-','-'])
new_table.add_column('lxc10 containers',['app5','dr7','drzoo2','nm2','sentinel3','zoo3','-'])
new_table.add_column('lxc11 containers',['af3','dr8','jn3','kaf3','-','-','-'])


print(new_table)
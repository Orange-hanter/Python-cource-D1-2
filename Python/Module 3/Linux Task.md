Add new raw hard disk to VM. 
- Make GPT partition table and 1 partition, 
- create ext4 fs on it, 
- mount in $HOME/test_partition and make this mountpoint persistent across reboots.


# Resolving

Войти в режим  редактирования диска

```
sudo fdisk /dev/sdX
```

В интерактивном меню нужно сначала выбрать систему дисков GPT (ввести `g`)
Для создания раздела вводим символ `n`
далее всё будет понятно по ходу дела, главное в конце сохранить изменения с помощью команды `w`

посмотреть новосозданный раздел можно как внутри утилиты fdisk (команда `p`), так и с помощью df команды

Теперь когда есть раздел файловой системы нужно создать саму файловую систему

`sudo mkfs.ext4 /dev/sdX0`

Для автоматического монтирования этого раздела нужно редактировать файл /etc/fstab. Добавим следующую строчку:
`<uuid-of-your-drive>  <mount-point>  <file-system-type>  <mount-option>  <dump>  <pass>`

Это конфигурация каждый раз при инициализации ОС будет монтировать диск в нужную дирректорию. 
- pass - порядок монтирования
- dump - нужно ли делать дамп памяти

Дабы сразу запустить монтирование выполняем команду 
`sudo mount -a`
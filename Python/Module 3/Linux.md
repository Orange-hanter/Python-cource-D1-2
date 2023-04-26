Q: What is character device
A: [1] **Character devices** are devices that do not have physically addressable storage media, such as tape drives or serial ports, where I/O is normally performed in a byte stream. This chapter describes the structure of a character device driver, focusing in particular on character driver entry points. In addition, this chapter describes the use of [physio(9F)](https://docs.oracle.com/docs/cd/E19683-01/816-0225/index.html) (in [read(9E)](https://docs.oracle.com/docs/cd/E19683-01/816-0224/index.html) and [write(9E)](https://docs.oracle.com/docs/cd/E19683-01/816-0224/index.html)) and [aphysio(9F)](https://docs.oracle.com/docs/cd/E19683-01/816-0225/index.html) (in [aread(9E)](https://docs.oracle.com/docs/cd/E19683-01/816-0224/index.html) and [awrite(9E)](https://docs.oracle.com/docs/cd/E19683-01/816-0224/index.html)) in the context of synchronous and asynchronous I/O transfers.
[1 Source](https://docs.oracle.com/cd/E19683-01/806-5222/character-21002/index.html#:~:text=Character%20devices%20are%20devices%20that,performed%20in%20a%20byte%20stream.)


Q: What is block device?
A: [1] Block devices are characterized by random access to data organized in fixed-size blocks. Examples of such devices are hard drives, CD-ROM drives, RAM disks, etc. The speed of block devices is generally much higher than the speed of character devices, and their performance is also important.
[[1] Source](https://linux-kernel-labs.github.io/refs/heads/master/labs/block_device_drivers.html#:~:text=Block%20devices%20are%20characterized%20by,their%20performance%20is%20also%20important.)


Q: dd command
A: Пример команды
`dd if=/dev/urandom of=/dev/null bs=100M count=5 `

Параметры:  

-   **if:** указывает на источник, т.е. на то, откуда копируем. Указывается файл, который может быть как обычным файлом, так и файлом устройства.
-   **of:** указывает на файл назначения. То же самое, писать можем как в обычный файл, так и напрямую в устройство.
-   **bs:** количество байт, которые будут записаны за раз. Можно представлять этот аргумент как размер куска данные, которые будут записаны или прочитаны, а количество кусков регулируется уже следующим параметром.
-   **count:** как раз то число, которое указывает: сколько кусочков будет скопировано.
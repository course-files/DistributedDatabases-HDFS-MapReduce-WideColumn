# HBase in Standalone Mode

## 1. Pull the required Docker Images and use them to Create and Run the Docker Containers

Delete the 4 previous containers then create and run the Docker containers specified in [Docker-Compose.yaml](Docker-Compose.yaml) i.e.,

* HBase-Master
* HBase-Regionserver
* Zookeeper

## 2. Connect to the HBase Shell Hosted in the `hbase-master` Docker container

HBase Shell is a JRuby-based command-line program you can use to interact with HBase.

```shell
docker exec -it hbase-master hbase shell
```

You can also confirm that HBase is running via its Web-UI: [http://localhost:16010/](http://localhost:16010/)

Execute the following statements in HBase shell:

```shell
# To show the version of HBase
## The output according to the setup should be:
## version 2.1.3
version

# To show the details of the servers running HBase:
# The output according to the setup should be:
# 1 active master, 0 backup masters, 1 servers, 0 dead, 2.0000 average load
status
```

## 3. Getting Help in HBase

To get guidance on a specific command:

```shell
# Replace COMMAND with the command you want guidance on
help 'COMMAND'
```

For general guidance on how to use table-referenced commands.

```shell
table_help
```

## 4. Create a Table

The table `product` has 2 column families:

* safety_features
* custom_paint

```shell
create 'product', 'safety_features', 'custom_paint'
```

Verify that the table has been created:

```shell
list
```

## 5. View the Table's Metadata

Execute the following to view the metadata of the created table:

```shell
describe 'product'
```

## 6. Insert Data

We use the keyword `put` to insert data in HBase. The following statement inserts a new record with the key **`first`** adding **`present`** to the column `'blind_spot_monitoring'` which is in the `'safety_features'` column family.

```shell
put 'product', 'first', 'safety_features:blind_spot_monitoring', 'present'
put 'product', 'first', 'safety_features:parking_assist', 'present'
```

Unfortunately, the `put` command in HBase shell allows you to insert only one column value at a time.

## 7. Retrieve Data

We use the keyword `get` to retrieve data from HBase. `get` requires the **table name** and the **row key**.

```shell
get 'product', 'first', 'safety_features:blind_spot_monitoring'
get 'product', 'first', 'safety_features:parking_assist'
```

We use the keyword `scan` to retrieve all the rows. This is compute-intensive for large databases and should be avoided in production. By default, HBase uses the current timestamp when inserting data and the most recent timestamp when retrieving data.

```shell
scan 'product'
```

## 8. Altering Tables

Altering tables is computationally expensive because HBase creates a new column family with the chosen specifications and then copies all the data to the new column.

* Disable the table

```shell
disable 'product'
```

By default, HBase stores only 3 versions of values (each with a timestamp). But this can be changed as follows:

```shell
alter 'product', { NAME => 'safety_features', VERSIONS => org.apache.hadoop.hbase.HConstants::ALL_VERSIONS }
```

We can also add a column-family (while the table is still disabled). The new column family called `make`.

```shell
alter 'product', { NAME => 'make', VERSIONS => org.apache.hadoop.hbase.HConstants::ALL_VERSIONS }
```

Similar to the `safety_features` column family, the `make` column family is added without any columns. It is upon the user to honour the schema. However, if the user decides not to honour the schema, e.g., by adding data to `make:new_column`, HBase will not stop them.

Lastly, we can set the compression method as follows:

```shell
alter 'product', {NAME=>'safety_features', COMPRESSION=>'GZ', BLOOMFILTER=>'ROW'}
```

* Enable the table

```shell
enable 'product'
```

## 9. Insert more Data with Schema-Flexibility in the `make` Column-Family

```shell
put 'product', 'second', 'safety_features:blind_spot_monitoring', 'present'
put 'product', 'second', 'safety_features:adaptive_cruise_control', 'present'
put 'product', 'second', 'safety_features:lane_keeping_assist', 'present'
```

```shell
scan 'product'
```

```shell
put 'product', 'second', 'custom_paint:red', '96'
put 'product', 'second', 'custom_paint:blue', '96'
put 'product', 'second', 'custom_paint:green', '96'
```

```shell
put 'product', 'first', 'make:YOM_brand', '2014 Mazda CX6'

put 'product', 'second', 'make:year_of_manufacture', '2019'
put 'product', 'second', 'make:brand', 'Toyota RAV4'
```

```shell
scan 'product'
```

## 10. Update Existing Data

HBase does not have a separate "update" command because `put` automatically overwrites any existing data in the specified row and column.

```shell
put 'product', 'first', 'safety_features:parking_assist', 'not present'
put 'product', 'second', 'custom_paint:blue', '100'
```

## 11. Delete Existing Data

HBase does not have a separate "update" command because `put` automatically overwrites any existing data in the specified row and column.

```shell
delete 'product', 'first', 'safety_features:parking_assist'
delete 'product', 'second', 'custom_paint:green'
```

### 不记文档，白忙一场

------

#### Zookeeper的sessiontimeout

> ```java
> import java.util.concurrent.CountDownLatch;
> 
> import org.apache.zookeeper.WatchedEvent; 
> import org.apache.zookeeper.Watcher; 
> import org.apache.zookeeper.ZooKeeper; 
> import org.apache.zookeeper.AsyncCallback.StatCallback; 
> import org.apache.zookeeper.Watcher.Event.KeeperState;
> 
> 
> public class testZ implements Watcher{ 
> 	protected CountDownLatch countDownLatch=new CountDownLatch(1); 
>  	ZooKeeper zooKeeper; 
>  	public void connect(String hosts) throws IOException, InterruptedException{ 
>  		zooKeeper = new ZooKeeper(hosts,4000,this); 
>  		countDownLatch.await(); 
>  	} 
>  
>      public void process(WatchedEvent event) { 
> 	    System.out.println(""); 
>         if(event.getState()==KeeperState.SyncConnected){ 
>             System.out.print("链接上了！"); 
>             //countDownLatch.countDown(); 
>         } else if (event.getState() == KeeperState.Disconnected) { 
>             System.out.print("失去链接了！");
>             //System.out.println("[SUC-CORE] session expired. now rebuilding");
> 
>             //session expired, may be never happending. 
>             //close old client and rebuild new client 
>             /// close();
> 
>             //getZooKeeper(); 
>         } else if (event.getState() == KeeperState.Expired) { 
>             System.out.print("session exception了！");
> 
>             System.out.println("[SUC-CORE] session expired. now rebuilding");
> 
>             //session expired, may be never happending. 
>             //close old client and rebuild new client 
>             close();
> 
>             //getZooKeeper(); 
>         } 
>      } 
> 
>      /** 
>      * 关闭zookeeper连接，释放资源 
>      */ 
>      public void close() { 
>         System.out.println("[SUC-CORE] close"); 
>         if (zooKeeper != null) { 
>             try { 
>                 zooKeeper.close(); 
>                 zooKeeper = null; 
>             } catch (InterruptedException e) { 
>                 //ignore exception 
>             } 
>         } 
>      } 
> 
>      public static void main(String args[]){ 
>         testZ a = new testZ(); 
>         try { 
>             a.connect("192.168.105.157:2181"); 
>         } catch (Exception e) {  
>             e.printStackTrace(); 
>         } 
>      }
> } 
> ```
>
> 
import java.util.Scanner;

public class Main{
	
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		
		int N=sc.nextInt(), M=sc.nextInt();
		
		int[] arr=new int[N];
		long max= 0;
		
		for(int i=0; i<N; i++)
		{
			arr[i]=sc.nextInt();
			if(max<arr[i]) max=arr[i];
		}
		long left=0, right=max;
		
		long result =0;
		while(left<=right)
		{
			long total = 0;
			long mid = (left+right)/2;
			for(int i=0; i<N; i++)
			{
				if(arr[i]-mid>=0)
				total+=arr[i]-mid;
			}
			
			if(total>=M)
			{
				if(mid>result) result=mid;
				left=mid+1;
			}
			else right=mid-1;
		}
		System.out.print(result);
	}
	
}

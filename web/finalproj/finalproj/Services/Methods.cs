using finalproj.Data;
using static System.Reflection.Metadata.BlobBuilder;

namespace finalproj.Services
{
	public class Methods
	{
		//need to create list of users and posts
		static List<Users> users = new List<Users>();
		static List<Posts> posts = new List<Posts>();
		static Dictionary<Users, List<Posts>> dict = new Dictionary<Users, List<Posts>>();

		public void AddUser()
		{
			int id = users.Any() ? users.Max(b => b.Id) + 1 : 1;
		}




	}
}

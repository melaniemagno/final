using final.Data;


namespace final.Services
{
	public interface InterfaceAPI
	{
		Task<int> GetUserCount();
		Task<Users> GetUsers(int id);
		Task<int> GetPostCount();
		Task<Posts> GetPosts(int id);
	}
}

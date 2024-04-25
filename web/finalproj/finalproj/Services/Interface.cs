using finalproj.Data;


namespace finalproj.Services
{
	public interface Interface
	{
		Task<int> GetUserCount();
		Task<Users> GetUsers(int id);
		Task<int> GetPostCount();
		Task<Posts> GetPosts(int id);
	}
}

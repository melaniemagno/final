using final.Data;
using System.Text.Json;
using System.Text;

namespace final.Services
{
	public class FileAPI : InterfaceAPI
	{
		private HttpClient httpClient;
		protected virtual string BASE_ADDR => "http://localhost:80";

		public FileAPI()
		{
			httpClient = new HttpClient();
		}

		public async Task<int> GetPostCount()
		{
			var apiResponseCount = await httpClient.GetFromJsonAsync<JsonElement>($"{BASE_ADDR}/posts_count");
			return apiResponseCount.GetInt32();
		}

		public async Task<Posts> GetPosts(int id)
		{
			var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"{BASE_ADDR}/posts/{id}");

			return new Posts
			{
				Id = id,
				Post = apiResponse.GetProperty("post").GetString()
			};
		}

		public async Task PostPost(Posts p)
		{
			try
			{
				string json = '{' + $"\"id\":\"{p.Id}\",\n" +
					$"\"post\":\"{p.Post}\"" + '}';
				StringContent JsonContent = new StringContent(json, Encoding.UTF8, "application/json");
				await httpClient.PostAsync($"{BASE_ADDR}/posts", JsonContent);
			}
			catch (HttpRequestException ex)
			{
				Console.WriteLine("could not create post." + ex.Message);
			}
		}

		public async Task DeletePost(int id)
		{
			await httpClient.DeleteAsync($"{BASE_ADDR}/posts/{id}");
		}

		public async Task<int> GetUserCount()
		{
			var apiResponseCount = await httpClient.GetFromJsonAsync<JsonElement>($"{BASE_ADDR}/users_count");
			return apiResponseCount.GetInt32();
		}

		public async Task<Users> GetUsers(int id)
		{
			var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"{BASE_ADDR}/users/{id}");

			return new Users
			{
				Id = id,
				Name = apiResponse.GetProperty("name").GetString(),
				Email = apiResponse.GetProperty("email").GetString(),
				Password = apiResponse.GetProperty("password").GetString(),
				Username = apiResponse.GetProperty("username").GetString()
			};
		}

		public async Task PostUser(Users u)
		{
			try
			{
				string json = '{' + $"\"id\":\"{u.Id}\",\n" +
					$"\"name\":\"{u.Name}\",\n" +
					$"\"email\":\"{u.Email}\",\n" +
					$"\"password\":\"{u.Password}\",\n" +
					$"\"username\":\"{u.Username}\"" + '}';
				StringContent JsonContent = new StringContent(json, Encoding.UTF8, "application/json");
				await httpClient.PostAsync($"{BASE_ADDR}/users", JsonContent);
			}
			catch (HttpRequestException ex)
			{
				Console.WriteLine("could not create user. User may already exist." + ex.Message);
			}
		}

		public async Task DeleteUser(int id)
		{
			await httpClient.DeleteAsync($"{BASE_ADDR}/users/{id}");
		}

	}
}

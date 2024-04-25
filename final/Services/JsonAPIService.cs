using System.Text.Json;
using final.Data;

namespace final.Services
{
    public class JsonAPIService : InterfaceAPI
    {

        private HttpClient httpClient;

        public JsonAPIService()
        {
            httpClient = new HttpClient();
        }

        public async Task<int> GetUserCount()
        {
            //Get the total number of current pokemon from the API
            var apiCountResponse = await httpClient.GetFromJsonAsync<JsonElement>("https://localhost:8000/users_count");
            return apiCountResponse.GetProperty("count").GetInt32();
        }

        public async Task<Users> GetUsers(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://localhost:8000/users/{id}");

            return new Users
            {
                Id = id,
                Name = apiResponse.GetProperty("name").GetString(),
                Email = apiResponse.GetProperty("email").GetString(),
                Password = apiResponse.GetProperty("password").GetString(),
                Username = apiResponse.GetProperty("username").GetString()
            };
        }

        public async Task<int> GetPostCount()
        {
            //Get the total number of current pokemon from the API
            var apiCountResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://localhost:8000/users/posts_count");
            return apiCountResponse.GetProperty("count").GetInt32();
        }

        public async Task<Posts> GetPosts(int id)
        {
            var apiResponse = await httpClient.GetFromJsonAsync<JsonElement>($"https://localhost:8000/posts/{id}");

            return new Posts
            {
                Id = id,
                Post = apiResponse.GetProperty("post").GetString()
            };
        }

    }
}

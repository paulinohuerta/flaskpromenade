MOCK_USERS = {'robert@example.com':'xyz'}

class MockDBHelper:
  
  def get_user(self,email):
    if email in MOCK_USERS:
      return MOCK_USERS[email]
    return None

puts("Request ID")
input_id = gets.chomp()

def login(_id)
  members = ['egoing', 'k8805', 'leezche']
  for member in members do
      if member == _id
        return true
      end
  end
  return false
end

if login(input_id)
      puts('Hello, '+input_id)
else
  puts('who are you?')
end

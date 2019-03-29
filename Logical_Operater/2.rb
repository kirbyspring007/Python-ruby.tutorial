puts("Request id")
input_id = gets.chomp()
puts("Request pwd")
input_pwd = gets.chomp()
real_id = "egoing"
real_pwd = "11"
if real_id == input_id
  if real_pwd == input_pwd
    puts("Hello!")
  else
    puts("Wrong pwd")
  end
else
  puts("Wrong id")
end

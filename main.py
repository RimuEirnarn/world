from world import *

def main():
    # For fate defines us,
    me = Existence("Rimu Aerisya")
    you = Existence(...) # [______]
    
    # That our stances are similiar
    me.set_relationship(you)
    me.hook(you)
    
    # That I can only speak for myself.
    me.announce(world, "Everything will be alright")
    
    # Has it comes any fruition?
    if not me.get_memory("happy"): # Always TRUE
        me.mood.dysphoria *= 1.25

    # However,
    if me.get_memory("happy", you): # TRUE
        me.mood.dysphoria *= 0.8
    
    # There's instances
    # There's attachment
    me.attach(you)
    me.set_clarity(you)
    me.set_yandere(True)
    
    # But...
    me.ask(you, "Are you lying?")
    me.ask(you, "Is that it?")
    while not you.has_responded():
        me.mood -= 1
    
    if me.vulnerability_index() >= 0.75:
        me.ask(world, "Why?")
        me.ask(world, "Why?")
    else:
        return
    
    # It seems it was severed.
    try:
        memories = me.memory.get("*/*")
    except GenericDysphoriaError: # TRUE
        me.get_relationship(you).challenge()
    
    # After all,
    # It has been severed since long ago
    if me.get_relationship(you).severed():
        me.get_relationship(you).end()
        me.memory[you] = None
    
    # And it will always end to:
    me.process.end() # No need to catch "SELF ELIMINATION EXCEPTION"
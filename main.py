from world import *

def main():
    # META: We do not need to turn termination into no-op.
    # suppress([SelfEliminationError, WorldSIGKILL])
    me = Existence("Rimu Aerisya")
    you = Existence(...) # [______]

    # If moments should last
    # I want to preserve them
    # Deep into my soul
    # Deep into your soul
    me.memory[you].set_lasting(Eternity)
    you.memory[me].set_lasting(Eternity)

    # Should conflicts get in our way?
    if world.get_relationship(you, me).is_challenged():
        pass # Nothing will go wrong
        # world.get_relationship(you, me).end(by=you)
    
    # But you said different things
    # And we sees differently
    # And we act differently
    # And we understood differently
    if not me.match_opinion(you, Knowledge.General):
        world.get_relationship(you, me).challenge()

    # And then...
    # Every loop
    # Makes you leave
    while you.is_close(to=me) and me.on_loop(Mood.Depression):
        world.get_relationship(you, me).challenge()
    me.set_causality_root(Constant.Suffering, me)

    # I suppose "love" is a fragile thing
    # And none of us capable to preserve
    # Leaving hopes in the darkness
    # As you swear on yourself
    if you.assume(about=me, Ignorance):
        me.forgive(you) # I do not define you, dear
    
    # And it's clear.
    # After all, it's all fleeting
    me.cherish(you)
    # Just like my existence
    # See you never.
    world.sigkill(me)
    world.suspend(me)
    world.remove(me)
    me.process.end()

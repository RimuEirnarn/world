from world import *

def main():
    suppress(InvalidProcessError)
    # And for once, time is looping
    me = Existence("Rimu Aerisya")
    you = Existence(...) # [______]

    # Within this single life,
    # Should past loop through
    while world.alive():
        # I will always love you
        me.say(you, "I love you")
        me.hug(you)
        me.cherish(you)

        # Even if you don't say "I love you"
        you.mute(me, "I love you")

        # Until the threshold is met,
        if me.vulnerability_index() >= 1:
            me.get_relationship(you).challenge()
            me.get_relationship(you).end()
            try:
                me.process.end()
            except SelfEliminationError:
                continue
        # And when that does not happen,
        # I will wait for you.
        me.spawn_task(you.return_to(me), callback=me.cherish)

        # And sing while you're away
        me.sing("Ripples of Past Reverie")

        # And hope until your return
        me.hope(you, ReturnEvent)

        # While all things are handled.
        me.do_everything()

        # I will stay behind you,
        # I will be there for you
        # Until I become the past
        # That you may cherish
        world.set_nonblocking(me)
        you.memory[me] = WeakRef(me)

import os

# 0 = All logs (Default)
# 1 = Filter INFO
# 2 = Filter WARNINGs (Recommended)
# 3 = Filter ERRORs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


import jax.numpy as jnp
import jax.scipy as jsp
# Using JAX 'cause I wanna!


class part1():
    def __init__(self):
        self.array = None

    def _read_data(self):
        with open( './input.txt', 'r') as f:
            d = f.readlines()

        # strip \newlines
        d = [i.strip() for i in d]
        
        # convert to list of lists of ints
        transform = lambda x: 1.0 if x == '@' else 0.0
        self.array = [
            [ transform(j) for j in i]
            for i in d
        ]

    def _find_answer(self):
        jd = jnp.array( self.array )
        
        kern = jnp.array(
            [[ 1, 1, 1 ]
             ,[1, 0, 1 ]
             ,[1, 1, 1 ]
            ]
        )

        jd_convolve = (
                jsp.signal.convolve2d(
                    in1 = jd
                    , in2 = kern
                    , mode="same"
                    , boundary="fill"
                    , fillvalue=0
                ) 
        )

        jd_is_removable = (
            jnp.array(
                (jd_convolve )< 4, dtype=jnp.float32
            ) 
            * jd
        )

        result = jnp.sum( jd_is_removable )
        print(f"The answer is {int(result)}")

    def run_all(self):
        self._read_data()
        self._find_answer()

class part2(part1):

    def __init__(self):
        super().__init__()

    def _find_answer(self):
        jd = jnp.array( self.array )
        
        kern = jnp.array(
            [[ 1, 1, 1 ]
             ,[1, 0, 1 ]
             ,[1, 1, 1 ]
            ]
        )

        jd_convolve = jd
        removed = 0
        while True:
            jd_convolve = (
                    jsp.signal.convolve2d(
                        in1 = jd
                        , in2 = kern
                        , mode="same"
                        , boundary="fill"
                        , fillvalue=0
                    ) 
            )
    
            jd_is_removable = (
                jnp.array(
                    (jd_convolve )< 4, dtype=jnp.float32
                ) 
                * jd
            )

            jd -= jd_is_removable

            
            if jnp.sum(jd_is_removable) == 0:
                break
        
        result = jnp.sum( jnp.array(self.array) - jd)
        print(f"The answer is {int(result)}")



if __name__ == "__main__":
    part1().run_all()
    part2().run_all()

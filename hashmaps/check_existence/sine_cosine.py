import torch


def euler_to_sin_cos(euler_angles: torch.Tensor) -> torch.Tensor:
    """
    Convert Euler angles to sine/cosine encoding.

    Args:
        euler_angles (torch.Tensor):
            A tensor of shape (..., 3) containing Euler angles in radians.

    Returns:
        torch.Tensor:
            A tensor of shape (..., 6) where the last dimension is
            [sin(theta_1), sin(theta_2), sin(theta_3),
             cos(theta_1), cos(theta_2), cos(theta_3)].
    """
    # euler_angles.shape => (..., 3)
    sin_part = torch.sin(euler_angles)  # (..., 3)
    cos_part = torch.cos(euler_angles)  # (..., 3)

    # Concatenate along the last dimension: -> (..., 6)
    sin_cos_rep = torch.cat([sin_part, cos_part], dim=-1)

    return sin_cos_rep


# Example usage:
if __name__ == "__main__":
    # Suppose we have a batch of 2 sets of Euler angles in radians
    euler_batch = torch.tensor([
        [0.610865, 0.785398, 0.959931],  # ~ [0 deg, 90 deg, 180 deg]
        [1.57, 3.14, 0.78]  # ~ [90 deg, 180 deg, 45 deg]
    ])

    sin_cos = euler_to_sin_cos(euler_batch)
    print("Input Euler angles (radians):\n", euler_batch)
    print("Output sine/cosine rep:\n", sin_cos)
-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'andrew@example.co', 'andrewbrown' ,'c4931da0-12de-471a-8b5b-ba82618834ee'),
  ('Andrew Bayko', 'bayko@example.co', 'bayko' ,'d1d3fd37-557e-4358-8fc9-399128ad9039'),
  ('ezz', 'ezzashraf444@gmail.com', 'EzzOps' ,'bd0d5a5f-3af7-4c3e-8dfc-1735f46df8af');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )